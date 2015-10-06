; demonstration of vectors and stuff

(print #(a b c))

(define (vector :rest xs)
  (list->vector xs))

(print (vector :a :b :c))
