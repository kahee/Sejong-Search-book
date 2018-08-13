import argparse
import os

MODES = ['local', 'dev', 'production']


def get_mode():
    """
    Get mode that you want to execute runserver mode
    1. 사용자가 옵션으로 mode를 전달한 경우
    2. 사용자가 옵션을 입력하지 않은 경우 입력을 통해 mode를 선택
    :return: mode
    """
    # build.py --mode <mode>
    # build.py -m <mode>
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help="Select the runserver mode({})".format(', '.join(MODES))
    )
    args = parser.parse_args()

    # 옵션으로 mode를 전달한 경우
    if args.mode:
        mode = args.mode.strip().lower()

    # 사용자 입력으로 mode를 선택한 경우
    else:
        while True:
            print('Select the mode you want to execute runserver mode')
            for index, mode_name in enumerate(MODES, start=1):
                print(f'{index}. {mode_name}')

            selected_mode = input('Choice mode: ')
            try:
                mode_index = int(selected_mode) - 1
                mode = MODES[mode_index]
                break
            except IndexError:
                print('The index number is wrong.')

    return mode


def mode_runserver(mode):
    """
    execute django-runserver after choose the mode from user
    :param mode:
    :return:
    """
    if mode in MODES:
        os.environ['DJANGO_SETTINGS_MODULE'] = f'config.settings.{mode}'
        if mode is 'local' or 'dev':
            os.system('pip install -r .requirements/dev.txt')
        else:
            os.system('pip install -r .requirements/production.txt')
        os.system('python app/manage.py runserver')

    else:
        raise ValueError(f'It must be possible to execute in {MODES}')


if __name__ == '__main__':
    mode = get_mode()
    mode_runserver(mode)
