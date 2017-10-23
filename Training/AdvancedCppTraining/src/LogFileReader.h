#pragma once

class QString;
#include "I_BatteryDataSource.h"

class LogFileReader : public I_BatteryDataSource
{
    Q_OBJECT
public:
    LogFileReader();
    virtual ~LogFileReader();

    bool readAll(const QString& fileName);

private:
    bool parseLine(const QString& line, BatteryData& batteryData) const;
};
