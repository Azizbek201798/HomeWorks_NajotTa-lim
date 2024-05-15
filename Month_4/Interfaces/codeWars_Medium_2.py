def asteroid_collision(asteroids):
    massiv = []

    for asteroid in asteroids:
        if asteroid > 0:
            massiv.append(asteroid)
        else:
            while massiv and massiv[-1] > 0 and massiv[-1] < abs(asteroid):
                massiv.pop()

            if not massiv or massiv[-1] < 0:
                massiv.append(asteroid)
            elif massiv[-1] == abs(asteroid):
                massiv.pop()

    return massiv
