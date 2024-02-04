echo "uninstalling existing packages \n"
packages="$(pip freeze | xargs -n 1 | cut -d"=" -f 1 | tr '\n' ' ')"
[[ ! -z "$packages" ]] && pip uninstall -y $packages

echo "installing packages \n"
requirement_path="./requirements.txt"
pip install -r $requirement_path

export PYTHONPATH="$PYTHONPATH:~/Projects/question_bank/web_server"