(define (Y f)
  ((lambda x (x x)) (lambda x (x x))))

(define (F f)
  (lambda n (if (= n 0)
                1
                (* n (f (- n 1))))))


;;; > ((Y F) 0)
;;;
;;; The object (#[compound-procedure 4]) is not applicable.
;;; To continue, call RESTART with an option number:
;;;  (RESTART 3) => Specify a procedure to use in its place.
;;;  (RESTART 2) => Return to read-eval-print level 2.
;;;  (RESTART 1) => Return to read-eval-print level 1.
