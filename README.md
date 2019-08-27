# TransportHartford Data Work

## Crash Fatalities

#### Crash Fatalities vs Public Transit Scatterplot
https://ilyankou.github.io/transporthartford/fatalities/viz/fatalities-v-transit.html

* Data used are from 2 sources: ACS and UCONN Crash Data.
The American Community Survey 2017 5-year estimates (ACS 17 5-year), which span 2013-2017,
does not represent average. It just means that the data points used for the estimates are
collected in these years. 5-year estimates are available for all sub-county divisions
in Connecticut, that means, we have Population and Transit Use estimates for all 169 towns in CT.
* UCONN Crash data was first deduplicated to avoid double (and triple) counting of fatalities.
The fatalities rates were then calculated on the average fatalities in years 2013-2017.
That is, for each town, I summed up # of fatalities for all years from 2013 to 2017,
and divided by 5. Then that number was divided by the 5-year ACS population estimate to get the rate per 100,000.


#### Crash Fatalities by Age by Sex, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/age-men-women.html

* This visualization is powered exclusively by UCONN Crash Data.
* Data was deduplicated and then grouped by gender and age.
* Unknown gender is mostly passengers.


#### Male Crash Fatalities by Age by Role, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/male-role.html

I considered Other Pedestrian (wheelchair, person in a building, skater, pedestrian conveyance)
as Pedestrian (4 instances); Occupant of a Non-Motor Vehicle Transportation Device as Passenger (1 instance).

#### Female Crash Fatalities by Age by Role, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/female-role.html


#### Male Driver Crash Fatalities by DUI Status, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/male-dui.html


#### Female Driver Crash Fatalities by DUI Status, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/female-dui.html


#### Male Driver Crash Fatalities by Speeding Status, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/male-speeding.html


#### Female Driver Crash Fatalities by Speeding Status, 2003-2017
https://ilyankou.github.io/transporthartford/fatalities/viz/female-speeding.html


## Speed Humps
#### Interactive table
https://ilyankou.github.io/transporthartford/crosswalks/interactive-table/

#### Leaflet Map
https://ilyankou.github.io/transporthartford/crosswalks/humps-map/

