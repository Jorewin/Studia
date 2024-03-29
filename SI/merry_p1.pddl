(define (problem p1)

    (:domain merry)

    (:objects
        A B C D E F G H I - room
        zielony czerwony pomaranczowy rozowy niebieski - color
        c1 c2 c3 c4 c5 c6 c7 c8 c9 - cell
        b1 b2 b3 b4 b5 b6 b7 b8 empty - block
    )

    (:init
        (lt n0 n1)
        (lt n1 n2)
        (lt n2 n3)
        (lt n3 n4)
        (lt n4 n5)
        (lt n5 n6)
        (lt n6 n7)
        (lt n7 n8)
        (lt n8 n9)
        (connected_both_ways H I niebieski)
        (connected_both_ways E F niebieski)
        (connected_both_ways H E czerwony)
        (connected_both_ways I F niebieski)
        (connected_both_ways E C zielony)
        (connected_both_ways F D zielony)
        (connected_both_ways C A czerwony)
        (connected_one_way F G rozowy)
        (connected_one_way A B pomaranczowy)
        (connected_one_way B D pomaranczowy)
        (ball_at H zielony n1)
        (ball_at H czerwony n1)
        (ball_at I pomaranczowy n1)
        (ball_at I niebieski n1)
        (ball_at E niebieski n1)
        (ball_at E zielony n1)
        (ball_at F niebieski n2)
        (ball_at C pomaranczowy n1)
        (ball_at C niebieski n1)
        (ball_at D zielony n1)
        (ball_at D czerwony n1)
        (ball_at A zielony n1)
        (ball_at B rozowy n1)
        (holding zielony n0)
        (holding czerwony n0)
        (holding pomaranczowy n0)
        (holding rozowy n0)
        (holding niebieski n0)
        (standing F)
        (visited F)
        (at c1 b5)
        (at c2 b4)
        (at c3 b1)
        (at c4 b8)
        (at c5 empty)
        (at c6 b3)
        (at c7 b7)
        (at c8 b2)
        (at c9 b6)
        (adjacent c1 c2)
        (adjacent c1 c4)
        (adjacent c2 c3)
        (adjacent c2 c5)
        (adjacent c3 c6)
        (adjacent c4 c5)
        (adjacent c4 c7)
        (adjacent c5 c6)
        (adjacent c5 c8)
        (adjacent c6 c9)
        (adjacent c7 c8)
        (adjacent c8 c9)
    )

    (:goal
        (and
            (visited A)
            (standing G)
            (at c1 b1)
            (at c2 b2)
            (at c3 b3)
            (at c4 b4)
            (at c5 b5)
            (at c6 b6)
            (at c7 b7)
            (at c8 b8)
            (at c9 empty)
        )
    )
)
