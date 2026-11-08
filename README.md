# To Do List - Yitzhak Rubin
 
## מטרת הפרוייקט
מערכת אישית להוספת, עריכת, מחיקת וניהול משימות.

כרגע מערכת מצומצמת ליוזר בודד

## DB

שימוש בdb רלציוני.
SQL/Supabase

## דרישות

### crud לניהול משימות

1. **Create** – יצירת משימה חדשה.
2. **Read** – הצגת כל המשימות.
3. **Update** – עריכת פרטי משימה קיימת.
4. **Delete** – מחיקת משימה.
5. שינוי סטטוס המשימה.

### חיפוש משימות

אפשרות לסנן משימות לפי סטטוס:
- כל המשימות
- ממתינות לביצוע
- בביצוע
- הושלמו

## Task table

| field | type | description |
| ----- | ---- | ----------- |
| id | UUID/int | unique id for task |
| title | string | headline |
| description | string | description for task |
| status | enum | task status (pending, in_progress, completed) |
| created_at | timestamp | creation date |
| updated_at | timestamp | update date |


## Backend - Endpoints

| Method | Endpoint | description |
|---|---|---|
| GET | `/tasks` | return all tasks |
| GET | `/tasks/:id` | return task by id |
| POST | `/tasks` | create task |
| PATCH | `/tasks/:id` | update task |
| DELETE | `/tasks/:id` | delete task |

## Frontend

מסך אחד שמציג את כל המשימות ככותרת וסטטוס בלבד עם כפתור למחיקה ועריכה (אמוג'י בלבד)
בלחיצה על משימה יוצגו שאר פרטי המשימה, התיאור, תאריך היצירה ותאריך העדכון האחרון
הכפתורים הראשוניים ייעלמו ויוצגו כפתורי עריכה ומחיקה עם אימוג'י ותיאור הפעולה (edit, delete).
עריכת סטטוס יכולה להיות גם במסך הראשוני וגם בפתיחת המשימה, ע"י שימוש בתפריט גלילה.

