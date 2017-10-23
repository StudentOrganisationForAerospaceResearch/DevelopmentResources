#pragma once

#include <QTime>

struct BatteryData
{
    BatteryData();
    BatteryData(QTime t, double v, double c);
    virtual ~BatteryData();

    QTime time;
    double voltage; // in V note all units should be stored in SI units
    double current; // in A
};
