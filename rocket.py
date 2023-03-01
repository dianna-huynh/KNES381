from time import sleep

def printRocket():
    print(
    """



                                 -
                              /     \

                               | * |


                               | * |

                               | * |

                              /    _\
                      """ )
printRocket()

delay = 1000
for i in range(60):
    print(
        """
                                 *
                                ***
                               *****
        """)
    sleep(delay/400)
    delay = delay *0.9

