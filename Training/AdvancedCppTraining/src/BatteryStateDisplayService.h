#pragma once

#include <QObject>
class I_BatteryDataSource;
class I_BatteryStateOfChargeService;
struct BatteryData;

class BatteryStateDisplayService : public QObject
{
    // This is used by QT in order to do the magic to connect slots.
    Q_OBJECT
public:
    BatteryStateDisplayService(const I_BatteryDataSource& batteryDataSource,
        I_BatteryStateOfChargeService& batteryStateOfChargeService);
    virtual ~BatteryStateDisplayService();

// Slots are what receive the signals. They can be private, protected or public
private slots:
    void handleBatteryDataReceived(const BatteryData& batteryData);

private:
    I_BatteryStateOfChargeService& batteryStateOfChargeService_;
};
