import cv2
import numpy as np
import time

# ==========================================
#   HAPPY JANMASHTAMI - CODE + CREATIVITY
# ==========================================

IMAGE_PATH = "krishna.jpg"

# ------------------------------------------
# LOAD IMAGE
# ------------------------------------------

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("ERROR: krishna.jpg not found!")
    print("Put krishna.jpg in the same folder as krishna_art.py")
    exit()

# ------------------------------------------
# RESIZE IMAGE
# ------------------------------------------

MAX_HEIGHT = 700

h, w = img.shape[:2]

if h > MAX_HEIGHT:
    scale = MAX_HEIGHT / h
    new_w = int(w * scale)
    img = cv2.resize(img, (new_w, MAX_HEIGHT))

h, w = img.shape[:2]

# ------------------------------------------
# CREATE KRISHNA LINE ART
# ------------------------------------------

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Smooth image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 60, 160)

# Make lines slightly stronger
edges = cv2.dilate(
    edges,
    np.ones((2, 2), np.uint8),
    iterations=1
)

# Get all edge pixels
points = np.column_stack(np.where(edges > 0))

# Randomize drawing order
np.random.shuffle(points)

# Black canvas
canvas = np.zeros((h, w, 3), dtype=np.uint8)

print("Creating Krishna artwork...")

# ------------------------------------------
# ANIMATION
# ------------------------------------------

total_points = len(points)

batch_size = max(100, total_points // 250)

for i in range(0, total_points, batch_size):

    batch = points[i:i + batch_size]

    for y, x in batch:

        # White + light blue artistic lines
        if (x + y) % 3 == 0:
            canvas[y, x] = (255, 200, 100)
        else:
            canvas[y, x] = (255, 255, 255)

    # Add title area
    display = canvas.copy()

    # Show animation
    cv2.imshow(
        "Code + Creativity | Happy Janmashtami",
        display
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

    time.sleep(0.02)


# ------------------------------------------
# FINAL ARTWORK
# ------------------------------------------

final = canvas.copy()

# Dark transparent banner at top
overlay = final.copy()

cv2.rectangle(
    overlay,
    (0, 0),
    (w, 100),
    (0, 0, 0),
    -1
)

final = cv2.addWeighted(
    overlay,
    0.65,
    final,
    0.35,
    0
)

# ------------------------------------------
# ADD TEXT
# ------------------------------------------

title = "HAPPY JANMASHTAMI"

font = cv2.FONT_HERSHEY_SIMPLEX

# Calculate text size
(text_w, text_h), _ = cv2.getTextSize(
    title,
    font,
    1,
    2
)

title_x = max(10, (w - text_w) // 2)

cv2.putText(
    final,
    title,
    (title_x, 45),
    font,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

subtitle = "Made with Python + Creativity"

(sub_w, sub_h), _ = cv2.getTextSize(
    subtitle,
    font,
    0.6,
    1
)

sub_x = max(10, (w - sub_w) // 2)

cv2.putText(
    final,
    subtitle,
    (sub_x, 75),
    font,
    0.6,
    (255, 200, 100),
    1,
    cv2.LINE_AA
)

# ------------------------------------------
# FINAL MESSAGE
# ------------------------------------------

message = "Happy Janmashtami to All"

(msg_w, msg_h), _ = cv2.getTextSize(
    message,
    font,
    0.7,
    2
)

msg_x = max(10, (w - msg_w) // 2)

cv2.putText(
    final,
    message,
    (msg_x, h - 30),
    font,
    0.7,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# ------------------------------------------
# SAVE OUTPUT
# ------------------------------------------

output_file = "happy_janmashtami_output.jpg"

cv2.imwrite(output_file, final)

print("\nSUCCESS!")
print("Your artwork has been saved as:")
print(output_file)

# Show final result in the SAME window
cv2.imshow(
    "Code + Creativity | Happy Janmashtami",
    final
)

print("\nSUCCESS!")
print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()