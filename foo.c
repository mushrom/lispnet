//#include <stdio.h>
//#include <stdlib.h>
//#include <errno.h>
//#include <sys/time.h>
//#include <unistd.h>

int puts( char *s );
void _exit( int status );

#define RULE(funcname, error) \
	int funcname( ) { \
		puts( #funcname ": operation not permitted." ); \
		_exit( 0 ); \
		return error; \
	}

/*
int fork( void ){
	printf( "fork: Operation not permitted\n" );
	_exit( 0 );
	return -1;
}

int futex(int *uaddr, int op, int val, const struct timespec *timeout,
                 int *uaddr2, int val3 ){
	errno = -1;
	return -1;
}
*/
RULE(fork,            -1)
RULE(execve,          -1)
RULE(chroot,          -1)

RULE(futex,           -1)
RULE(lstat,           -1)
//RULE(geteuid,         -1)
RULE(gettid,          -1)
//RULE(getpid,          -1)
RULE(getrusage,       -1)
RULE(socket,          -1)
RULE(getrlimit,       -1)
RULE(tgkill,          -1)
//RULE(ioctl,           -1)
RULE(chmod,           -1)
RULE(shmdt,           -1)
//RULE(madvise,         0)
RULE(fstatfs,         0)
RULE(fcntl,           0)
//RULE(mkdir,           0)
RULE(symlink,         0)
RULE(setitimer,       0)
RULE(unlink,          0)
RULE(dup2,            0)
//RULE(munmap,          0)
RULE(umask,           0)
RULE(vfork,           0)
RULE(rt_sigprocmask,  0)
RULE(set_robust_list, 0)

/*
	{ RULE(read,            ALLOW)
	, RULE(readv,           ALLOW)
	, RULE(pread64,         ALLOW)
	, RULE(write,           ALLOW)
	, RULE(writev,          ALLOW)
	, RULE(pwrite64,        ALLOW)
	, RULE(access,          ALLOW)
	, RULE(stat,            ALLOW)
	, RULE(fstat,           ALLOW)
	, RULE(open,            ALLOW)
	, RULE(openat,          ALLOW)
	, RULE(lseek,           ALLOW)
	, RULE(close,           ALLOW)
	, RULE(exit_group,      ALLOW)
	, RULE(execve,          ALLOW)
	, RULE(brk,             ALLOW)
	, RULE(mmap,            ALLOW)
	, RULE(mremap,          ALLOW)
	, RULE(arch_prctl,      ALLOW)
	, RULE(readlink,        ALLOW)
	, RULE(mprotect,        ALLOW)
		// Needed by glibc's malloc, though curiously only when
		// allocation fails (e.g. due to resource limits).
	, RULE(getcwd,          ALLOW)
	, RULE(gettimeofday,    ALLOW)
	, RULE(getdents,        ALLOW)
	, RULE(set_tid_address, ALLOW)
	, RULE(fallocate,       ALLOW)
	, RULE(clock_gettime,   ALLOW)
	, RULE(exit,            ALLOW)
	, RULE(sched_yield,     ALLOW)
	, RULE(futex,           ERRNO(-1))
	, RULE(lstat,           ERRNO(-1))
	, RULE(geteuid,         ERRNO(-1))
	, RULE(gettid,          ERRNO(-1))
	, RULE(getpid,          ERRNO(-1))
	, RULE(getrusage,       ERRNO(-1))
	, RULE(socket,          ERRNO(-1))
	, RULE(getrlimit,       ERRNO(-1))
	, RULE(tgkill,          ERRNO(-1))
	, RULE(ioctl,           ERRNO(-1))
	, RULE(chmod,           ERRNO(-1))
	, RULE(shmdt,           ERRNO(-1))
	, RULE(madvise,         ERRNO(0))
	, RULE(fstatfs,         ERRNO(0))
	, RULE(fcntl,           ERRNO(0))
	, RULE(mkdir,           ERRNO(0))
	, RULE(symlink,         ERRNO(0))
	, RULE(setitimer,       ERRNO(0))
	, RULE(unlink,          ERRNO(0))
	, RULE(dup2,            ERRNO(0))
	, RULE(munmap,          ERRNO(0))
	, RULE(umask,           ERRNO(0))
	, RULE(vfork,           ERRNO(0))
	, RULE(rt_sigprocmask,  ERRNO(0))
	, RULE(set_robust_list, ERRNO(0))
	, RULE(rt_sigaction,    ALLOW) // must be allowed for diagnose_sigsys to work
	};

*/
