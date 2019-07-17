from gym.envs.registration import register

register(
    id='HumanoidMaze-v0',
    entry_point='humanoid_maze.envs:HumanoidMazeEnv',
)
