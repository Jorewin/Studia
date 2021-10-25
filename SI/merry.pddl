(define (domain merry)

    (:types room color number cell block)

    (:constants n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 - number)

    (:predicates
        (lt ?p ?q - number)
        (ball_at ?x - room ?a - color ?p - number)
        (holding ?a - color ?p - number)
        (standing ?x - room)
        (visited ?x - room)
        (connected_both_ways ?x ?y - room ?a - color)
        (connected_one_way ?x ?y - room ?a - color)
        (adjacent ?x ?y - cell)
        (at ?x - cell ?p - block)
    )

    (:derived (connected ?x ?y - room ?a - color)
        (or
            (connected_one_way ?x ?y ?a)
            (connected_both_ways ?x ?y ?a)
            (connected_both_ways ?y ?x ?a)
        )
    )

    (:derived (adjacent_derived ?x ?y - cell)
        (or
            (adjacent ?x ?y)
            (adjacent ?y ?x)
        )
    )

    (:action wez
        :parameters (?a - color ?x - room ?p ?q ?r ?s - number)
        :precondition
            (and
                (ball_at ?x ?a ?p)
                (standing ?x)
                (holding ?a ?r)
                (lt ?q ?p)
                (lt ?r ?s)
            )
        :effect
            (and
                (not (ball_at ?x ?a ?p))
                (ball_at ?x ?a ?q)
                (not (holding ?a ?r))
                (holding ?a ?s)
            )
    )

    (:action idz
        :parameters (?y ?x - room ?a - color ?p ?q - number)
        :precondition
            (and
                (standing ?x)
                (connected ?x ?y ?a)
                (holding ?a ?p)
                (lt ?q ?p)
            )
        :effect
            (and
                (not (standing ?x))
                (standing ?y)
                (visited ?y)
                (not (holding ?a ?p))
                (holding ?a ?q)
            )
    )

    (:action przesun
        :parameters (?p - block ?x ?y - cell)
        :precondition
            (and
                (standing A)
                (adjacent_derived ?x ?y)
                (at ?x ?p)
                (at ?y empty)
            )
        :effect
            (and
                (not (at ?x ?p))
                (at ?x empty)
                (not (at ?y empty))
                (at ?y ?p)
            )
    )
)
