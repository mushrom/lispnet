#!/bin/sh

cp "codefiles/$1" "wut/code/$2"

ulimit -m 32000
ulimit -v 145000
ulimit -t 100
ulimit -f 32

#ulimit -a

#cd wut/$1
#gojira $1

#TODO: filter output to not leak sensitive information
#fakechroot chroot wut bash -c 'LD_PRELOAD=libfoo.so:$LD_PRELOAD qemu-x86_64 /usr/bin/gojira '"code/$2" 2>&1
fakechroot chroot wut bash -c 'LD_PRELOAD=libfoo.so:$LD_PRELOAD qemu-x86_64 /usr/bin/gojira '"code/$2"
