## game
WELL_W          = 10
WELL_H          = 20
MOVE_DELAY      = 0.13
MOVE_INTERVAL   = 0.04
MAX_FPS         = 120
ROW_CLR_SPEED   = 20
MESSAGE_BLINK   = 0.7
SCORE_POINTS    = [100, 250, 500, 1000]
LEVEL_SCORES    = [  0,   500,  1000,  2000,  3000,  5000,  7000, 11000, 16000, 23000, 32000]
SPEED_LEVELS    = [1.0, 0.904, 0.808, 0.712, 0.616,  0.52, 0.424, 0.328, 0.232, 0.136,  0.04]
DRAW_FPS        = False

## default window
CELL_W          = 45
SCREEN_W        = CELL_W * (WELL_W + 18)
SCREEN_H        = CELL_W * (WELL_H + 1)

## colors
BG_COLOR1       = (0, 0, 0)
BG_COLOR2       = (14, 16, 11)
WELL_COLOR1     = (46, 59, 59)
WELL_COLOR2     = (51, 64, 64)
WELL_COLOR3     = (88, 110, 110)
CELL_COLOR1     = (255, 222, 161)
CELL_COLOR2     = (175, 194, 170)
GLOW_COLOR      = (125, 145, 145)
TEXT_COLOR1     = (175, 194, 170)
TEXT_COLOR2     = (6, 10, 10)
TEXT_COLOR3     = (43, 46, 43)

## glyphs
GLYPHS = {
    'I' : [ 
            [ [1, 1, 1, 1]              ],
            [ [1], [1], [1], [1]        ],
            [ [1, 1, 1, 1]              ],
            [ [1], [1], [1], [1]        ] 
          ],
    'J' : [
            [ [1, 1, 1], [0, 0, 1]      ],
            [ [0, 1], [0, 1], [1, 1]    ],
            [ [1, 0, 0], [1, 1, 1]      ],
            [ [1, 1], [1, 0], [1, 0]    ]
          ],
    'L' : [
            [ [1, 1, 1], [1, 0, 0]      ],
            [ [1, 1], [0, 1], [0, 1]    ],
            [ [0, 0, 1], [1, 1, 1]      ],
            [ [1, 0], [1, 0], [1, 1]    ]
          ],
    'O' : [
            [ [1, 1], [1, 1]            ],
            [ [1, 1], [1, 1]            ],
            [ [1, 1], [1, 1]            ],
            [ [1, 1], [1, 1]            ]
          ],
    'S' : [
            [ [0, 1, 1], [1, 1, 0]      ],
            [ [1, 0], [1, 1], [0, 1]    ],
            [ [0, 1, 1], [1, 1, 0]      ],
            [ [1, 0], [1, 1], [0, 1]    ]
          ],
    'T' : [
            [ [1, 1, 1], [0, 1, 0]      ],
            [ [0, 1], [1, 1], [0, 1]    ],
            [ [0, 1, 0], [1, 1, 1]      ],
            [ [1, 0], [1, 1], [1, 0]    ]
          ],
    'Z' : [
            [ [1, 1, 0], [0, 1, 1]      ],
            [ [0, 1], [1, 1], [1, 0]    ],
            [ [1, 1, 0], [0, 1, 1]      ],
            [ [0, 1], [1, 1], [1, 0]    ]
          ]
}
