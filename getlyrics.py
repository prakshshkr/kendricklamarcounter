import lyricsgenius, re, os

genius = lyricsgenius.Genius("VvpppPtO2MPLWIHBc_gokEn-_jHnvPpyI2-Fr7iuxK4wsBSGIBf_pSmhJAztz5Fe")

with open("names", "r") as a_file:
	for line in a_file:
		stripped_line = line.strip()
		song = genius.search_song(stripped_line, "Kendrick Lamar")
		path="songlyrics/"+song.title.replace('/','')+".txt"
		print(path)
		lyrics=re.sub(r'\[.*?\]', '', song.lyrics)
		f = open(path, "w")
		f.write(lyrics)
		f.close()
		os.system('cat songlyrics/*.txt > all.txt')
		count="cat all.txt| tr '[:space:]' '[\n*]' | grep -v \"^\\s*$\" | sort | uniq -c | sort -bnr > count.txt"
		os.system(count)