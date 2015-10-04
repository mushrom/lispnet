#!/bin/sh

mkdir "$1"

cd gojira
./configure --prefix=/usr --sysroot="../$1" --static
make install
cd ..

mkdir -p "$1/lib64" "$1/code"
ln -s "`pwd`/$1/lib64" "`pwd`/$1/lib"

ln -s /lib64/ld-linux-x86-64.so.2                    "$1/lib64/ld-2.22.so"
ln -s /lib64/libfakeroot/fakechroot/libfakechroot.so "$1/lib64/libfakechroot.so"

ln -s "`which bash`"        "$1/usr/bin/bash"
ln -s "`which qemu-x86_64`" "$1/usr/bin/qemu-x86_64"

gcc -shared -fPIC foo.c -o "$1/lib64/libfoo.so"
