#pragma once

#include <QTime>
struct BatteryData;

class I_BatteryStateOfChargeService
{
public:
    virtual ~I_BatteryStateOfChargeService() {}

    virtual double totalAmpHoursUsed() const = 0;
    virtual bool isCharging() const = 0;
    virtual QTime timeWhenChargedOrDepleted() const = 0;

    virtual void addData(const BatteryData& batteryData) = 0;
};
