"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input( "Please enter your age: "))
max = 220 - age
goal_min = 0.65 * max
goal_max = 0.85 * max
print(f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {goal_min:.0f} and {goal_max:.0f} beats per minute.")