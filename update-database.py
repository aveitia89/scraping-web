from new import New, NewDetails
import slug

for new in New.objects():
    try:
        new.LinkUrl = slug.slug(new.Title)
        new.save()
    except StopIteration as it:
        print(it)