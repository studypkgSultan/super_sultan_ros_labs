# Мои лабораторные работы по ROS 2

**Студент:** Султан  
**Курс:** ROS 2 Jazzy  


## 📚 Список лабораторных работ

| Лабораторная | Описание | Код | Статус |
|--------------|----------|-----|--------|
| [lab_01_hello_ros](./lab_01_hello_ros) | Первый пакет, узлы Hello World и таймер | `super_sultan_study_pkg` | ✅ Выполнено |
| [lab_02_pub_sub](./lab_02_pub_sub) | Publisher и Subscriber | `super_sultan_pub_sub_pkg` | 🔄 В процессе |
| lab_03_... | ... | ... | 📅 Запланировано |

## 🛠️ Требования для запуска
- Ubuntu 24.04
- ROS 2 Jazzy
- Python 3

## 🚀 Быстрый старт
```bash
# Клонировать репозиторий
git clone https://github.com/ВАШ_ЛОГИН/super_sultan_ros_labs.git
cd super_sultan_ros_labs

# Собрать конкретную лабу
cd lab_01_hello_ros
colcon build --packages-select super_sultan_study_pkg
source install/setup.bash
ros2 run super_sultan_study_pkg time_printer
