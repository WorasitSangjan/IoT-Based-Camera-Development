# Crontab Manual

A guide for automating tasks on Raspberry Pi/Linux systems using crontab.

## Table of Contents
- [Basic Setup](#basic-setup)
- [Syntax Guide](#syntax-guide)
- [Scheduling Examples](#scheduling-examples)
- [Maintenance and Monitoring](#maintenance-and-monitoring)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Basic Setup

To begin editing your crontab configuration:
```bash
crontab -e
```
Note: First-time users may be prompted to choose an editor. Nano is recommended for beginners.

## Syntax Guide

Each crontab entry follows this structure:
```
MIN HOUR DAY MONTH DAYOFWEEK COMMAND
```

### Field Specifications

| Field | Allowed Values | Example |
|-------|----------------|---------|
| MIN (Minutes) | 0-59 | 30 = 30th minute |
| HOUR | 0-23 | 14 = 2:00 PM |
| DAY (Day of Month) | 1-31 | 5 = 5th day |
| MONTH | 1-12 | 8 = August |
| DAYOFWEEK | 0-7 (0 and 7 = Sunday) | 1 = Monday |
| COMMAND | The command/script to run | /path/to/script.sh |

## Scheduling Examples

### Python Script Scheduling Examples

```bash
# Run every minute
* * * * * /usr/bin/python3 /home/pi/myscript.py

# Run every 10 minutes
*/10 * * * * /usr/bin/python3 /home/pi/myscript.py

# Run at 6:00 AM daily
0 6 * * * /usr/bin/python3 /home/pi/myscript.py

# Run at 6 AM, 12 PM, and 6 PM
0 6,12,18 * * * /usr/bin/python3 /home/pi/myscript.py

# Run every Sunday at 3:30 PM
30 15 * * 0 /usr/bin/python3 /home/pi/myscript.py

# Run on the first day of every month
0 0 1 * * /usr/bin/python3 /home/pi/myscript.py
```

## Maintenance and Monitoring

### View Current Crontab Entries
```bash
crontab -l
```

### Check Cron Service Status
```bash
systemctl status cron
```

### Enable and Start Cron Service
```bash
sudo systemctl enable cron
sudo systemctl start cron
```

## Troubleshooting

### 1. Output Logging
To log both standard output and errors:
```bash
0 6 * * * /usr/bin/python3 /home/pi/myscript.py >> /home/pi/logs/myscript.log 2>&1
```

### 2. View Logs
Check script-specific logs:
```bash
cat /home/pi/logs/myscript.log
```

Check system cron logs:
```bash
grep CRON /var/log/syslog | tail -20
```

## Best Practices

1. Always use full paths for scripts and programs
   - Example: `/usr/bin/python3` instead of just `python3`

2. Regularly verify scheduled jobs
   - Use `crontab -l` to list and verify all jobs

3. Monitor job execution
   - Check logs regularly
   - Set up error notifications for critical jobs

4. Use appropriate permissions
   - Use `sudo crontab -e` for system-wide tasks
   - Ensure correct file permissions for scripts

5. Test scripts independently
   - Verify scripts work outside of cron before scheduling
   - Test with the same user that will run the cron job
