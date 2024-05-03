import matplotlib.pyplot as plt
from jax import numpy as jnp
from train import train_acc, train_cost, val_acc, val_cost, test_estimation
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from config import n_epochs
from digits import y_test


def Plot_results() -> plt.figure():
    """
    Plot training and validating results after each epoch.
    :return: plt.figure()
    """
    step = 10
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12,4.5))
    axs[0].plot(train_cost, label="Train cost teacher", color='royalblue')
    axs[0].plot(val_cost, label="Validation cost teacher", color='tab:blue')
    axs[1].plot(train_acc, label='Train accuracy teacher', color='orangered')
    axs[1].plot(val_acc, label='Validation accuracy teacher', color='orange')
    axs[0].set_xlabel("Epoch")
    axs[1].set_xlabel("Epoch")
    axs[0].set_xticks(jnp.arange(0, n_epochs + step, step))
    axs[1].set_xticks(jnp.arange(0, n_epochs + step, step))
    axs[0].legend()
    axs[1].legend()
    return fig


def PLot_Confusion_Matrix() -> ConfusionMatrixDisplay:
    """
    Creates confusion matrix and displays it.
    :return: (ConfusionMatrixDisplay) displayed confusion matrix.
    """
    conf_matrix = confusion_matrix(y_true=y_test, y_pred=test_estimation)
    display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix).plot()
    return display
