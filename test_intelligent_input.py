from intelligent_input import YoutubeURLValidator, YoutubeMetadataExtractor

v = YoutubeURLValidator()
res = v.validate('https://youtu.be/dQw4w9WgXcQ?t=10s')
print('Validation:', res)

if res['valid']:
    m = YoutubeMetadataExtractor()
    meta = m.extract(res['normalized_url'])
    print('Title:', meta.get('title'))
    print('Duration:', meta.get('duration'), 'seconds')
