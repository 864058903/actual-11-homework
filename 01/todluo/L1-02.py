#!/usr/bin/env python
# encoding:utf-8
has_watermelon = raw_input('can  you show watermelon ? (Y/N)')
if has_watermelon == 'Y' :
    print 'i can show watermelon !'
    has_ssb = raw_input('you has 1 Steamed stuffed bun? (Y/N)')
    if has_ssb == 'Y':
        print  'buy 1 Steamed stuffed bun !'
    else:
        print  'buy 0 Steamed stuffed bun'
else:
    print 'i do not can show watermelon'
    has_ssb = raw_input('you has 5 Steamed stuffed bun? (Y/N)')
    if has_ssb == 'Y':
        print 'buy 5 Steamed stuffed bun'
    else:
        print 'buy 0 Steamed stffed bun'
print 'over'
