import os

from subprocess import call
from argparse import ArgumentParser

PROJECT_NAME = 'cs231'
PIPFILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assignments')

docker_run = f"""
    docker run -v "{PIPFILE_DIR}:/srv/{PROJECT_NAME}" \
"""
docker_run_postfix = f" -it --rm {PROJECT_NAME}:1.0 "
# см. секцию ARG в ./Dockerfile
docker_args = f' --build-arg DOCKER_PROJECT_NAME="{PROJECT_NAME}" '

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--scenario', dest='scenario', required=True, help='Сценарий работы')
    args = parser.parse_args()
    sh_command = None
    if args.scenario in ('pipenv', 'bash'):
        sh_command = f'{docker_run} {docker_run_postfix} {args.scenario}'
    elif args.scenario == 'build':
        sh_command = f'docker build {docker_args} -t {PROJECT_NAME}:1.0 .'
    elif args.scenario == 'jupyter':
        sh_command = f'{docker_run} -p 8889:8888 {docker_run_postfix} {args.scenario}'
    else:
        raise ValueError('Ошибочный сценарий: %s' % args.scenario)
    print(sh_command)
    call(sh_command, shell=True)