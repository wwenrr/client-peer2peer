#!/bin/bash
export TERM=xterm-256color
clear

if [ ! -d "lib" ]; then
    echo "Không tìm thấy file thư viện, bắt đầu cài đặt"
    sudo apt install python3-venv
    clear
    python3 -m venv lib
    source lib/bin/activate
    pip install -r package.txt
    clear
else 
    source lib/bin/activate
fi

python3 -B -m src.run --reload