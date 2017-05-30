import gym



env = gym.mke ('CartPole-v0')
env.reset()
for _ in range(1000):
	env.render()
	env.step(env.aaction_space.sample)
