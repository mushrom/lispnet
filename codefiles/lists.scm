; a demonstration of lists and stuff
(import! 'lists)

(print '(1 2 3))
(print (map (lambda (x)
              (* x x))
              (take infinity 10)))
