import logging
from scrapper import dialogbox


def main():
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info("presenting the dialog box")
    box = dialogbox.DialogBox()
    box.create()


if __name__ == '__main__':
    main()
