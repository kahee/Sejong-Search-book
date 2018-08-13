import argparse
import subprocess
import sys

MODES = ['base', 'local', 'dev', 'production']


def get_mode():
    """
    Get mode that you want to build docker images
    1. 사용자가 옵션으로 mode를 전달한 경우
    2. 사용자가 옵션을 입력하지 않은 경우 입력을 통해 mode를 선택
    :return: mode
    """
    # build.py --mode <mode>
    # build.py -m <mode>
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help="Docker build mode({})".format(', '.join(MODES))
    )
    args = parser.parse_args()

    # 옵션으로 mode를 전달한 경우
    if args.mode:
        mode = args.mode.strip().lower()

    # 사용자 입력으로 mode를 선택한 경우
    else:
        while True:
            print('Select the mode you want to build')
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


def mode_function(mode):
    """
    build docker images after choose the mode from user
    :param mode:
    :return:
    """
    if mode in MODES:
        cur_module = sys.modules[__name__]
        getattr(cur_module, f'build_{mode}')()

    else:
        raise ValueError(f'It must be possible to execute in {MODES}')


def build_base():
    """
    build base docker images and push that images to the docker hub
    :return:
    """
    try:
        subprocess.call('docker build -t sejong-docker:base -f Dockerfile.base .', shell=True)

    finally:
        print('Successfully build base')
        subprocess.call('docker tag sejong-docker:base ygh131/sejong_search_book_project', shell=True)
        subprocess.call('docker push ygh131/sejong_search_book_project', shell=True)
        print('Successfully push docker images')


def build_local():
    """
    build local docker images
    :return:
    """
    try:
        subprocess.call('docker build -t sejong-docker:local -f Dockerfile.local .', shell=True)
    finally:
        print('Successfully build local')


def build_dev():
    """
    build dev docker images
    :return:
    """
    try:
        subprocess.call('docker build -t sejong-docker:dev -f Dockerfile.dev .', shell=True)
    finally:
        print('Successfully build dev')


def build_production():
    """
    build production docker images
    :return:
    """
    try:
        subprocess.call('docker build -t sejong-docker:production -f Dockerfile.production .', shell=True)
    finally:
        print('Successfully build production')


if __name__ == '__main__':
    mode = get_mode()
    mode_function(mode)
