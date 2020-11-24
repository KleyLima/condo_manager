from source.view.error import error


def plot_errors(text_error):
    """
    Just plot the error(s) in the proper frame for that
    :param text_error: String containing the errors of the user
    :return: None
    """
    error.list_errors.setText(text_error)
    error.show()
