# PC PART SEARCHER
PC Hardware Scrapper works in some of the Local PC Stores in Egypt, including:
- Amazon EG
- Sigma PC
- El Badr Group
- OLX aka Dubbizle
- and more ..

![image](https://github.com/user-attachments/assets/943d04d0-9edc-4581-a87e-829951fe3eef)


<p>Use the following instructions:</p>
<ul>
    <li>Search Endpoint: <code>/api/search</code></li>
    <li>Search Options:
<ul>
    <li>search_term: string (e.g., 'rtx')</li>
    <li>source_filters:
  <ul>
                                <li>amazon: boolean (true/false)</li>
                                <li>baraka: boolean (true/false)</li>
                                <li>olx: boolean (true/false)</li>
                                <li>sigma: boolean (true/false)</li>
                                <li>badr: boolean (true/false)</li>
                                <li>alfrensia: boolean (true/false)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Coming Soon: Compumarts</p>
            


# Example Response with rtx search temr:
```
{
    "status": "success",
    "amazon": [
        {
            "Page": 1,
            "Price": "8,100.",
            "Title": "Gigabyte GeForce RTX 3050 OC 6GB GDDR6 Graphics Card - 14000MHz Memory, PCI-E, Custom Cooling, Direct Copper Heat Pipe, Effective Heat Dissipation, 6GB VRAM, 3.5/5 Stars, GV-N3050OC-6GL",
            "Rating": "4.4 out of 5 stars",
            "source": "amazon",
            "Image URL": "https://m.media-amazon.com/images/I/61GQFZKhywL._AC_UL320_.jpg",
            "Details Link": "https://www.amazon.eg/-/en/Gigabyte-GeForce-3050-GDDR6-Graphics/dp/B0CV4CPQ7S/ref=sr_1_1?dib=eyJ2IjoiMSJ9.0gYlp7YxW-oq9LF_WPz4Ys8hxQVDFNzR1WrzlrOje_M-G7qMug2qPL-K6Tk5drEqb-jlDE23LDIZ2B2yeobsslX7oW3EUTfPNIa90MMsjAL7Tik70cda0VvM6j86go6lWx66Deh4c-C-dqdJ7LCZa5p6UewCWFxdMJqKfXO0WZYrHms-eVDpL8mZQpHdcA6G4pC4t8M1xEcE2NW0m2Q1xy8DaFcGmdlkRGUG78hVsEYRLHcGZ5h23VuHQQlpOx4xPwiYiiBqiBNVcb5CkAXFVlLtTRUmA6pky-6NAaFCrWA.XI9or5YDZ7S_d2RHTjI8_l6sZ-Ly-erIGTdjeitHn_k&dib_tag=se&keywords=rtx&qid=1747856094&sr=8-1"
        },
        {
            "Page": 1,
            "Price": "10,299.",
            "Title": "Gigabyte GeForce RTX 3050 WINDFORCE OC 6GB Graphics Card - 1477MHz GPU, 14000MHz Memory, PCI-E 4.0, 2 Fans, DisplayPort & HDMI, GDDR6, 7680x4320 Max Resolution, for Gaming, GV-N3050WF2OC-6GD",
            "Rating": "4.7 out of 5 stars",
            "source": "amazon",
            "Image URL": "https://m.media-amazon.com/images/I/81fLtWboBxL._AC_UL320_.jpg",
            "Details Link": "https://www.amazon.eg/-/en/Gigabyte-GeForce-WINDFORCE-Graphics-GV-N3050WF2OC-6GD/dp/B0D5J5XS36/ref=sr_1_2?dib=eyJ2IjoiMSJ9.0gYlp7YxW-oq9LF_WPz4Ys8hxQVDFNzR1WrzlrOje_M-G7qMug2qPL-K6Tk5drEqb-jlDE23LDIZ2B2yeobsslX7oW3EUTfPNIa90MMsjAL7Tik70cda0VvM6j86go6lWx66Deh4c-C-dqdJ7LCZa5p6UewCWFxdMJqKfXO0WZYrHms-eVDpL8mZQpHdcA6G4pC4t8M1xEcE2NW0m2Q1xy8DaFcGmdlkRGUG78hVsEYRLHcGZ5h23VuHQQlpOx4xPwiYiiBqiBNVcb5CkAXFVlLtTRUmA6pky-6NAaFCrWA.XI9or5YDZ7S_d2RHTjI8_l6sZ-Ly-erIGTdjeitHn_k&dib_tag=se&keywords=rtx&qid=1747856094&sr=8-2"
        },
        {
            "Page": 1,
            "Price": "32,919.",
            "Title": "GIGABYTE GeForce RTX 4070 WINDFORCE OC 12GB Graphics Card - 12GB DDRX6 21Gbps, PCI-E 4.0, DisplayPort 1.4, HDMI 2.1a, NVIDIA DLSS 3, Ada Lovelace Arch, GV-N4070WF3OC-12GD, Black, 930g",
            "Rating": "4.7 out of 5 stars",
            "source": "amazon",
            "Image URL": "https://m.media-amazon.com/images/I/71liIYrRmkL._AC_UL320_.jpg",
            "Details Link": "https://www.amazon.eg/-/en/GIGABYTE-GeForce-WINDFORCE-Graphics-GV-N4070WF3OC-12GD/dp/B0BZHCQ6PF/ref=sr_1_3?dib=eyJ2IjoiMSJ9.0gYlp7YxW-oq9LF_WPz4Ys8hxQVDFNzR1WrzlrOje_M-G7qMug2qPL-K6Tk5drEqb-jlDE23LDIZ2B2yeobsslX7oW3EUTfPNIa90MMsjAL7Tik70cda0VvM6j86go6lWx66Deh4c-C-dqdJ7LCZa5p6UewCWFxdMJqKfXO0WZYrHms-eVDpL8mZQpHdcA6G4pC4t8M1xEcE2NW0m2Q1xy8DaFcGmdlkRGUG78hVsEYRLHcGZ5h23VuHQQlpOx4xPwiYiiBqiBNVcb5CkAXFVlLtTRUmA6pky-6NAaFCrWA.XI9or5YDZ7S_d2RHTjI8_l6sZ-Ly-erIGTdjeitHn_k&dib_tag=se&keywords=rtx&qid=1747856094&sr=8-3"
        },
        and more ...
```
