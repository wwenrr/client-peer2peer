#!/bin/bash
export TERM=xterm-256color
clear

if [ ! -d "lib" ]; then
    echo "Không tìm thấy file thư viện, bắt đầu cài đặt"
    python3 -m venv lib
    source lib/bin/activate
    pip install -r package.txt
fi





