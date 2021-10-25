(define (domain hanoi)

    (:types disk rod)

    (:constants x y z - rod)

    (:predicates
        (lt ?x ?y - disk)
        (on_disk ?x ?y - disk)
        (on_rod ?x - disk ?y - rod)
        (clear ?x)
    )

    (:derived (lt_derived ?x ?y - disk)
        (or
            (lt ?x ?y)
            (exists (?z - disk) (and (lt ?x ?z) (lt_derived ?z ?y)))
        )
    )

    (:derived (on_rod_derived ?x - disk ?y - rod)
        (or
            (on_rod ?x ?y)
            (exists (?z - disk) (and (on_disk ?x ?z) (on_rod_derived ?z ?y)))
        )
    )

    (:action rod_to_rod
        :parameters (?x ?y - rod ?a - disk)
        :precondition
            (and
                (on_rod ?a ?x)
                (clear ?y)
                (clear ?a)
            )
        :effect
            (and
                (not (on_rod ?a ?x))
                (on_rod ?a ?y)
                (clear ?x)
                (not (clear ?y))
            )
    )

    (:action rod_to_disk
        :parameters (?x ?y - rod ?a ?b - disk)
        :precondition
            (and
                (on_rod ?a ?x)
                (on_rod_derived ?b ?y)
                (clear ?a)
                (clear ?b)
                (lt_derived ?a ?b)
            )
        :effect
            (and
                (not (on_rod ?a ?x))
                (clear ?x)
                (not (clear ?b))
                (on_disk ?a ?b)
            )
    )

    (:action disk_to_rod
        :parameters (?x ?y - rod ?a ?b - disk)
        :precondition
            (and
                (on_disk ?a ?b)
                (on_rod_derived ?b ?x)
                (clear ?a)
                (clear ?y)
            )
        :effect
            (and
                (not (on_disk ?a ?b))
                (on_rod ?a ?y)
                (clear ?b)
                (not (clear ?y))
            )
    )

    (:action disk_to_disk
        :parameters (?x ?y - rod ?a ?b ?c - disk)
        :precondition
            (and
                (on_disk ?a ?b)
                (on_rod_derived ?b ?x)
                (on_rod_derived ?c ?y)
                (clear ?a)
                (clear ?c)
                (lt_derived ?a ?c)
            )
        :effect
            (and
                (not (on_disk ?a ?b))
                (on_disk ?a ?c)
                (clear ?b)
                (not (clear ?c))
            )
    )
)
