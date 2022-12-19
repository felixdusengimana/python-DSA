def licenseKeyFormatting(strs: str, k: int):
    splited_str = strs.upper().split("-")
    reformatted_licence_key = splited_str[0]
    splited_str.pop(0)
    i = 0
    out_combined_text = ""
    while i < len(splited_str):
        combined_text = out_combined_text + splited_str[i]
        if len(combined_text) == k:
            reformatted_licence_key += ("-" + combined_text)
            out_combined_text = ""

        if len(combined_text) < k:
            out_combined_text = combined_text

        i += 1

    return reformatted_licence_key


print(licenseKeyFormatting("2-5g-3-J", 4))
