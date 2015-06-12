[ -f ~/.env/sphinx/bin/activate ] && . ~/.env/sphinx/bin/activate

make clean
make CONFIG=bootstrap html
make latexpdf
make epub
