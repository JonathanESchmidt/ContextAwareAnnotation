# ContextAwareAnnotation
Repository for annotation tools used for context aware navigation

### The files are used to prepare the annotation images for training a YOLO network.

- The *Remove_empty_frames.py* file is used to remove any empty images by giving a template frame to pass through all images in a folder.
- The *Rotate.py* and *Translate.py* are used to augment the the dataset while saving with a new filename for saving images as series for training.
- The *Annotate_frames.py* file is used for annotating bounding boxes for different setups - enables one or multiple boxes depending on usecase.
- The *ShowAnnotation.py* is used for sanity check and to see the Bounding Boxes.
