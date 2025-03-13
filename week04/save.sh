
mlalias cs2041.24T2.tutors | sed -En '/Addresses/,/Owners/p'| head -n -1 | tail -n +2 | sed -En 's/^\s*(z[0-9]{7})\s*$/\1/p'


acc z5417087 | sed -En '/^$/,/^$/p' | cut -d':' -f2 | tr ',' '\n' | sed -En 's/^.*([A-Z]{4}[0-9]{4})t[1-3]_Student.*$/\1/p'
