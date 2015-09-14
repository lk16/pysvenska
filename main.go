func parseLocation(file string) (locations map[string]*Point, err error) {
    f, err := os.Open(file)
    if err != nil {
        return nil, err
    }
    defer f.Close() // this needs to be after the err check

    lines, err := csv.NewReader(f).ReadAll()
    if err != nil {
        return nil, err
    }

    //already defined in declaration, no need for :=
    locations = make(map[string]*Point, len(lines))
    var lat, lon float64 //predeclare lat, lon
    for _, line := range lines {
        // shorter, cleaner and since we already have lat and err declared, we can do this.
        if lat, err = strconv.ParseFloat(line[1], 64); err != nil {
            return nil, err
        }
        if lon, err = strconv.ParseFloat(line[2], 64); err != nil {
            return nil, err
        }
        locations[line[0]] = &Point{lat, lon}
    }
    return locations, nil
}