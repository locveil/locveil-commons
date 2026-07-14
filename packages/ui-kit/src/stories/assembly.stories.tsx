import type { Meta, StoryObj } from "@storybook/react";
import { Bug, SlidersHorizontal } from "lucide-react";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";
import { Alert, AlertDescription } from "../components/ui/alert";
import { StatusChip } from "../components/ui/status-chip";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../components/ui/tabs";
import { Icon } from "../components/ui/icon";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../components/ui/select";

const meta: Meta = { title: "Assembly/Workbench slice" };
export default meta;

/* The round-2 council mock, rebuilt on the real components. */
export const ConfigForm: StoryObj = {
  render: () => (
    <div className="max-w-md space-y-3">
      <div className="flex items-center gap-2">
        <Tabs defaultValue="voice">
          <TabsList>
            <TabsTrigger value="voice">Голос</TabsTrigger>
            <TabsTrigger value="bridge">Мост</TabsTrigger>
          </TabsList>
          <TabsContent value="voice" className="mt-3">
            <Card>
              <CardHeader>
                <CardTitle>Микрофон</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="space-y-1">
                  <Label htmlFor="dev">Устройство</Label>
                  <Select defaultValue="usb">
                    <SelectTrigger id="dev">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="usb">USB Audio (hw:1,0)</SelectItem>
                      <SelectItem value="int">Встроенный (hw:0,0)</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="space-y-1">
                  <Label htmlFor="vad">Порог VAD</Label>
                  <Input id="vad" defaultValue="0.52" className="tabular-nums" />
                </div>
                <div className="flex items-center gap-2">
                  <Button>Сохранить</Button>
                  <Button variant="outline">Проверить</Button>
                  <StatusChip variant="edited">изменено</StatusChip>
                </div>
                <Alert variant="accent">
                  <AlertDescription>
                    Изменения не применены — проверьте конфигурацию
                  </AlertDescription>
                </Alert>
              </CardContent>
            </Card>
          </TabsContent>
          <TabsContent value="bridge" className="mt-3">
            <Card>
              <CardContent className="pt-4 text-sm text-muted-foreground">
                Плагин «Мост» — страницы настройки появятся после bridge UI-17.
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
        <span className="ml-auto flex gap-2 self-start text-muted-foreground">
          <Icon icon={SlidersHorizontal} size="button" />
          <Icon
            icon={Bug}
            size="button"
            className="transition-colors duration-200 hover:text-[hsl(38_92%_50%)]"
          />
        </span>
      </div>
    </div>
  ),
};
