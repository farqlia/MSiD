from typing import List, Tuple


def validate_inputs_to_cm(y_true, y_pred, num_classes):
    if len(y_true) != len(y_pred):
        raise ValueError(f"Invalid input shapes!: {len(y_true)} != {len(y_pred)}")

    min_class = min(min(y_true), min(y_pred))
    max_class = max(max(y_true), max(y_pred))

    if min_class < 0 or max_class >= num_classes:
        raise ValueError(f"Invalid prediction classes!")


def get_confusion_matrix(
    y_true: List[int], y_pred: List[int], num_classes: int,
) -> List[List[int]]:
    """
    Generate a confusion matrix in a form of a list of lists. 

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values
    :param num_classes: number of supported classes

    :return: confusion matrix
    """
    validate_inputs_to_cm(y_true, y_pred, num_classes)
    confusion_matrix = [[0 for _ in range(num_classes)] for _ in range(num_classes)]
    for actual_class, pred_class in zip(y_true, y_pred):
        confusion_matrix[actual_class][pred_class] += 1

    return confusion_matrix



def get_quality_factors(
    y_true: List[int],
    y_pred: List[int],
) -> Tuple[int, int, int, int]:
    """
    Calculate True Negative, False Positive, False Negative and True Positive 
    metrics basing on the ground truth and predicted lists.

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: a tuple of TN, FP, FN, TP
    """
    # Number of classes is 2 because we assume binary classification
    confusion_matrix = get_confusion_matrix(y_true, y_pred, 2)
    flattened_cm = [metric for row in confusion_matrix for metric in row]
    # Convert the list to a tuple
    return (*flattened_cm, )


def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the accuracy for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: accuracy score
    """
    TN, FP, FN, TP = get_quality_factors(y_true, y_pred)
    return (TN + TP) / (TN + FP + FN + TP)


def precision_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the precision for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: precision score
    """
    _, FP, _, TP = get_quality_factors(y_true, y_pred)
    return TP / (TP + FP)


def recall_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the recall for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: recall score
    """
    _, _, FN, TP = get_quality_factors(y_true, y_pred)
    return TP / (TP + FN)


def f1_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the F1-score for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: F1-score
    """
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = 2 * precision * recall / (precision + recall)
    return f1

