import os
import playhatdemo

demo_name = os.environ.get('PLAYHAT_DEMO', 'random').lower()

if demo_name == 'random':
    demo = playhatdemo.random
elif demo_name == 'servo':
    demo = playhatdemo.servo
else:
    raise ValueError(
        'Unrecognised demo name: %s -- Available options: "random", "servo"' %
        demo_name)

print('Running demo "%s"' % demo_name)

demo.main()
