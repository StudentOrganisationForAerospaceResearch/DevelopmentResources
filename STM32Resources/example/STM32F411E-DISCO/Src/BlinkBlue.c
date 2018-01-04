#include "cmsis_os.h"

#include "stm32f4xx.h"
#include "stm32f4xx_hal_conf.h"
#include "stm32f4xx_hal_gpio.h"

#include "BlinkBlue.h"

void blinkBlueLedTask(void const* arg)
{
    uint32_t prevWakeTime = osKernelSysTick();

    for (;;)
    {
        osDelayUntil(&prevWakeTime, BLINK_BLUE_FREQ);
        HAL_GPIO_TogglePin(LD6_GPIO_Port, LD6_Pin);
        // HAL_GPIO_TogglePin(LD5_GPIO_Port, LD5_Pin);
        // HAL_GPIO_TogglePin(LD4_GPIO_Port, LD4_Pin);
        // HAL_GPIO_TogglePin(LD3_GPIO_Port, LD3_Pin);
    }
}
