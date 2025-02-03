import pandas as pd


def annotate_taxonomy(
        data: pd.DataFrame,
        annotations: list[str],
        annotations_label: list[str] = ['origin'],
) -> pd.DataFrame:
    if len(annotations) != len(annotations_label):
        raise ValueError('Annotations and labels must be the same length.')
    for (annotation, annotation_label) in zip(annotations, annotations_label):
        data[annotation_label] = annotation
    return data
