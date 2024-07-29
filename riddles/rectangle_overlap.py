def calc_overlap(co1, dim1, co2, dim2):
    greater = max(co1, co2)
    lower = min(co1 + dim1, co2 + dim2)

    if greater >= lower:
        return (None, None)

    overlap = lower - greater

    return greater, overlap


def calc_rect_overlap(r1, r2):
    x_overlap, w_overlap = calc_overlap(r1['x'], r1['w'], r2['x'], r2['w'])
    y_overlap, h_overlap = calc_overlap(r1['y'], r1['h'], r2['y'], r2['h'])

    if not w_overlap or not h_overlap:
        print('No overlap')
        return None

    return {
        'x': x_overlap,
        'y': y_overlap,
        'w': w_overlap,
        'h': h_overlap
    }


r1 = {'x': 2, 'y': 4, 'w': 5, 'h': 12}
r2 = {'x': 1, 'y': 5, 'w': 7, 'h': 14}

result = calc_rect_overlap(r1, r2)
print(result)
