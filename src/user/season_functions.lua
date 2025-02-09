function assign_season_prefix(item)
    item = capitalise(item)
    if item == "Name" then return "Season" end
    return item
end

function search_season_info(item)
    local season_options = { name = season.Name, starts = season.Starts, ends = season.Ends, element = season.Element, planet = season.Planet, modality = season.Modality, unicode = season.Unicode }

    if season_options[item] then return season_options[item] end
    return "Error"
end
