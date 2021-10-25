(define (problem p1)
	(:domain hanoi)
	(:objects a b c d e - disk)
	(:init
        (lt a b)
        (lt b c)
        (lt c d)
        (lt d e)
        (clear a)
		(on_disk a b)
		(on_disk b c)
		(on_disk c d)
		(on_disk d e)
		(on_rod e x)
        (clear y)
        (clear z)
	)
	(:goal
		(and
            (clear a)
		    (on_disk a b)
		    (on_disk b c)
		    (on_disk c d)
		    (on_disk d e)
		    (on_rod e z)
			(clear x)
	        (clear y)
        )
	)
)
