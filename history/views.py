from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from pathlib import Path
import difflib


@login_required
def history(request):
    media_root = Path(settings.BASE_DIR) / 'media'
    media_root.mkdir(exist_ok=True)
    file_names = sorted([f.name for f in media_root.glob('*.json')])
    file_a = request.GET.get('file_a') or (file_names[0] if file_names else None)
    file_b = request.GET.get('file_b') or (file_names[1] if len(file_names) > 1 else None)

    lines_a = []
    lines_b = []
    removed = set()
    added = set()

    if file_a and file_b:
        path_a = media_root / file_a
        path_b = media_root / file_b
        if path_a.exists() and path_b.exists():
            lines_a = path_a.read_text().splitlines()
            lines_b = path_b.read_text().splitlines()
            diff = list(difflib.ndiff(lines_a, lines_b))
            removed = {line[2:] for line in diff if line.startswith('- ')}
            added = {line[2:] for line in diff if line.startswith('+ ')}

    context = {
        'file_names': file_names,
        'file_a': file_a,
        'file_b': file_b,
        'lines_a': [{'text': line, 'removed': line in removed} for line in lines_a],
        'lines_b': [{'text': line, 'added': line in added} for line in lines_b],
    }
    return render(request, 'history/history.html', context)
