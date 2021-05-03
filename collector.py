import random

def get_sticker(set_size = 700):
	return random.sample(range(set_size), k=1)

def collect(set_size = 700, cutoff = 696):
	unique_stickers = set([])
	total_stickers = 0

	while len(unique_stickers) != set_size:
		total_stickers += 1
		current_unique = len(unique_stickers)
		for sticker in get_sticker(set_size):
			unique_stickers.add(sticker)
		if len(unique_stickers) != current_unique:
			if len(unique_stickers) == cutoff:
				md_jd = total_stickers
	return (md_jd, total_stickers)

def simulate(trials = 100, set_size = 700, cutoff = 696):
	mdjd_results = []
	total_results = []
	for i in range(1, trials+1):
		res = collect(set_size, cutoff)
		mdjd_results.append(res[0])
		total_results.append(res[1])
	return ( float( sum(mdjd_results)/trials),float( sum(total_results)/trials))


sim = simulate(trials = 1000, set_size = 700, cutoff = 696)
print('Average stickers needed to get to 696: ', sim[0])
print ('Average stickers needed to get to 700:', sim[1])
